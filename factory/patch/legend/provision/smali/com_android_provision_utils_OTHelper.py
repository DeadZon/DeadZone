TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/utils/OTHelper.smali'
CLASS_FALLBACK_NAMES = ['OTHelper.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_android_provision_utils_OTHelper__tkEvent',
        'method': '.method public static final tkEvent(Ljava/lang/String;)V',
        'method_name': 'tkEvent',
        'method_anchors': ['sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z', 'if-nez v0, :cond_0', 'sget-object v0, Lcom/android/provision/utils/OTHelper;->sInited:Ljava/util/concurrent/atomic/AtomicBoolean;', 'invoke-virtual {v0}, Ljava/util/concurrent/atomic/AtomicBoolean;->get()Z', 'if-eqz v0, :cond_1', 'invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z', 'if-nez v0, :cond_1', 'sget-object v0, Lcom/android/provision/utils/OTHelper;->sOneTrack:Lcom/xiaomi/onetrack/OneTrack;'],
        'type': 'method_delete',
        'search': """.method public static final tkEvent(Ljava/lang/String;)V
    .registers 3

    sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    sget-object v0, Lcom/android/provision/utils/OTHelper;->sInited:Ljava/util/concurrent/atomic/AtomicBoolean;

    invoke-virtual {v0}, Ljava/util/concurrent/atomic/AtomicBoolean;->get()Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_1

    :try_start_0
    sget-object v0, Lcom/android/provision/utils/OTHelper;->sOneTrack:Lcom/xiaomi/onetrack/OneTrack;

    if-eqz v0, :cond_1

    const/4 v1, 0x0

    invoke-virtual {v0, p0, v1}, Lcom/xiaomi/onetrack/OneTrack;->track(Ljava/lang/String;Ljava/util/Map;)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    return-void

    :catch_0
    const-string p0, "OTHelper"

    const-string v0, "tkEvent exception"

    invoke-static {p0, v0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    :cond_1
    :goto_0
    return-void
.end method""",
        'replacement': """""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_utils_OTHelper__tkEvent',
        'method': '.method public static final tkEvent(Ljava/lang/String;Ljava/util/Map;)V',
        'method_name': 'tkEvent',
        'method_anchors': ['sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z', 'if-nez v0, :cond_0', 'sget-object v0, Lcom/android/provision/utils/OTHelper;->sInited:Ljava/util/concurrent/atomic/AtomicBoolean;', 'invoke-virtual {v0}, Ljava/util/concurrent/atomic/AtomicBoolean;->get()Z', 'if-eqz v0, :cond_1', 'invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z', 'if-nez v0, :cond_1', 'sget-object v0, Lcom/android/provision/utils/OTHelper;->sOneTrack:Lcom/xiaomi/onetrack/OneTrack;'],
        'type': 'method_delete',
        'search': """.method public static final tkEvent(Ljava/lang/String;Ljava/util/Map;)V
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/lang/String;",
            "Ljava/util/Map<",
            "Ljava/lang/String;",
            "Ljava/lang/Object;",
            ">;)V"
        }
    .end annotation

    sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    sget-object v0, Lcom/android/provision/utils/OTHelper;->sInited:Ljava/util/concurrent/atomic/AtomicBoolean;

    invoke-virtual {v0}, Ljava/util/concurrent/atomic/AtomicBoolean;->get()Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_1

    :try_start_0
    sget-object v0, Lcom/android/provision/utils/OTHelper;->sOneTrack:Lcom/xiaomi/onetrack/OneTrack;

    if-eqz v0, :cond_1

    invoke-virtual {v0, p0, p1}, Lcom/xiaomi/onetrack/OneTrack;->track(Ljava/lang/String;Ljava/util/Map;)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    return-void

    :catch_0
    const-string p0, "OTHelper"

    const-string p1, "tkEvent exception"

    invoke-static {p0, p1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    :cond_1
    :goto_0
    return-void
.end method""",
        'replacement': """""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_utils_OTHelper__initialize',
        'method': '.method public static initialize(Landroid/content/Context;)V',
        'method_name': 'initialize',
        'method_anchors': ['sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z', 'if-nez v0, :cond_0', 'invoke-virtual {p0}, Landroid/content/Context;->getApplicationContext()Landroid/content/Context;', 'sget-object v1, Lcom/android/provision/utils/OTHelper;->mConfig:Lcom/xiaomi/onetrack/Configuration;', 'invoke-static {v0, v1}, Lcom/xiaomi/onetrack/OneTrack;->createInstance(Landroid/content/Context;Lcom/xiaomi/onetrack/Configuration;)Lcom/xiaomi/onetrack/OneTrack;', 'sput-object v0, Lcom/android/provision/utils/OTHelper;->sOneTrack:Lcom/xiaomi/onetrack/OneTrack;', 'invoke-static {v0}, Lcom/xiaomi/onetrack/OneTrack;->setDebugMode(Z)V', 'invoke-static {}, Lcom/xiaomi/onetrack/OneTrack;->setUseSystemNetTrafficOnly()V'],
        'type': 'method_replace',
        'search': """.method public static initialize(Landroid/content/Context;)V
    .registers 3

    sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    :try_start_0
    invoke-virtual {p0}, Landroid/content/Context;->getApplicationContext()Landroid/content/Context;

    move-result-object v0

    sget-object v1, Lcom/android/provision/utils/OTHelper;->mConfig:Lcom/xiaomi/onetrack/Configuration;

    invoke-static {v0, v1}, Lcom/xiaomi/onetrack/OneTrack;->createInstance(Landroid/content/Context;Lcom/xiaomi/onetrack/Configuration;)Lcom/xiaomi/onetrack/OneTrack;

    move-result-object v0

    sput-object v0, Lcom/android/provision/utils/OTHelper;->sOneTrack:Lcom/xiaomi/onetrack/OneTrack;

    const/4 v0, 0x0

    invoke-static {v0}, Lcom/xiaomi/onetrack/OneTrack;->setDebugMode(Z)V

    invoke-static {}, Lcom/xiaomi/onetrack/OneTrack;->setUseSystemNetTrafficOnly()V

    invoke-static {p0, v0}, Lcom/xiaomi/onetrack/OneTrack;->setAccessNetworkEnable(Landroid/content/Context;Z)V

    sget-object p0, Lcom/android/provision/utils/OTHelper;->sInited:Ljava/util/concurrent/atomic/AtomicBoolean;

    const/4 v0, 0x1

    invoke-virtual {p0, v0}, Ljava/util/concurrent/atomic/AtomicBoolean;->set(Z)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    return-void

    :catch_0
    move-exception p0

    const-string v0, "OTHelper"

    const-string v1, "initialize error"

    invoke-static {v0, v1, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :goto_0
    return-void
.end method""",
        'replacement': """.method public static initialize(Landroid/content/Context;)V
    .registers 1

    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_utils_OTHelper__rdBottomButtonEvent',
        'method': '.method public static rdBottomButtonEvent(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V',
        'method_name': 'rdBottomButtonEvent',
        'method_anchors': ['sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z', 'if-nez v0, :cond_0', 'if-eqz p0, :cond_1', 'invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z', 'if-eqz v0, :cond_1', 'invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;', 'invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;', 'invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z'],
        'type': 'method_replace',
        'search': """.method public static rdBottomButtonEvent(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V
    .registers 4

    sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    if-eqz p0, :cond_1

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p1

    :cond_1
    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p0

    if-eqz p0, :cond_2

    :goto_0
    return-void

    :cond_2
    new-instance p0, Ljava/util/HashMap;

    invoke-direct {p0}, Ljava/util/HashMap;-><init>()V

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string p1, "_"

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    const-string p2, "button_name"

    invoke-interface {p0, p2, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string p1, "event_page_bottom_button_click"

    invoke-static {p1, p0}, Lcom/android/provision/utils/OTHelper;->tkEvent(Ljava/lang/String;Ljava/util/Map;)V

    return-void
.end method""",
        'replacement': """.method public static rdBottomButtonEvent(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V
    .registers 3

    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_utils_OTHelper__rdCountEvent',
        'method': '.method public static rdCountEvent(Ljava/lang/String;)V',
        'method_name': 'rdCountEvent',
        'method_anchors': ['sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z', 'if-nez v0, :cond_0', 'return-void', 'invoke-static {p0}, Lcom/android/provision/utils/OTHelper;->tkEvent(Ljava/lang/String;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method public static rdCountEvent(Ljava/lang/String;)V
    .registers 2

    sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z

    if-nez v0, :cond_0

    return-void

    :cond_0
    invoke-static {p0}, Lcom/android/provision/utils/OTHelper;->tkEvent(Ljava/lang/String;)V

    return-void
.end method""",
        'replacement': """.method public static rdCountEvent(Ljava/lang/String;)V
    .registers 1

    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_utils_OTHelper__rdCountEvent',
        'method': '.method public static rdCountEvent(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V',
        'method_name': 'rdCountEvent',
        'method_anchors': ['sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z', 'if-nez v0, :cond_0', 'return-void', 'new-instance v0, Ljava/util/HashMap;', 'invoke-direct {v0}, Ljava/util/HashMap;-><init>()V', 'invoke-interface {v0, p1, p2}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;', 'invoke-static {p0, v0}, Lcom/android/provision/utils/OTHelper;->tkEvent(Ljava/lang/String;Ljava/util/Map;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method public static rdCountEvent(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
    .registers 4

    sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z

    if-nez v0, :cond_0

    return-void

    :cond_0
    new-instance v0, Ljava/util/HashMap;

    invoke-direct {v0}, Ljava/util/HashMap;-><init>()V

    invoke-interface {v0, p1, p2}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    invoke-static {p0, v0}, Lcom/android/provision/utils/OTHelper;->tkEvent(Ljava/lang/String;Ljava/util/Map;)V

    return-void
.end method""",
        'replacement': """.method public static rdCountEvent(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
    .registers 3

    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_utils_OTHelper__rdCountEvent',
        'method': '.method public static rdCountEvent(Ljava/lang/String;Ljava/util/Map;)V',
        'method_name': 'rdCountEvent',
        'method_anchors': ['sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z', 'if-nez v0, :cond_0', 'return-void', 'new-instance v0, Ljava/util/HashMap;', 'invoke-direct {v0}, Ljava/util/HashMap;-><init>()V', 'if-eqz p1, :cond_1', 'invoke-interface {p1}, Ljava/util/Map;->entrySet()Ljava/util/Set;', 'invoke-interface {p1}, Ljava/util/Set;->iterator()Ljava/util/Iterator;'],
        'type': 'method_replace',
        'search': """.method public static rdCountEvent(Ljava/lang/String;Ljava/util/Map;)V
    .registers 5
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/lang/String;",
            "Ljava/util/Map<",
            "Ljava/lang/String;",
            "Ljava/lang/String;",
            ">;)V"
        }
    .end annotation

    sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z

    if-nez v0, :cond_0

    return-void

    :cond_0
    new-instance v0, Ljava/util/HashMap;

    invoke-direct {v0}, Ljava/util/HashMap;-><init>()V

    if-eqz p1, :cond_1

    :try_start_0
    invoke-interface {p1}, Ljava/util/Map;->entrySet()Ljava/util/Set;

    move-result-object p1

    invoke-interface {p1}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object p1

    :goto_0
    invoke-interface {p1}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_1

    invoke-interface {p1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Ljava/util/Map$Entry;

    invoke-interface {v1}, Ljava/util/Map$Entry;->getKey()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Ljava/lang/String;

    invoke-interface {v1}, Ljava/util/Map$Entry;->getValue()Ljava/lang/Object;

    move-result-object v1

    invoke-interface {v0, v2, v1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    const-string p1, "OTHelper"

    const-string v1, "rdCountEvent exception"

    invoke-static {p1, v1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    :cond_1
    invoke-static {p0, v0}, Lcom/android/provision/utils/OTHelper;->tkEvent(Ljava/lang/String;Ljava/util/Map;)V

    return-void
.end method""",
        'replacement': """.method public static rdCountEvent(Ljava/lang/String;Ljava/util/Map;)V
    .registers 2

    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_utils_OTHelper__rdInputmethodEvent',
        'method': '.method public static rdInputmethodEvent(Ljava/lang/String;)V',
        'method_name': 'rdInputmethodEvent',
        'method_anchors': ['sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z', 'if-nez v0, :cond_0', 'return-void', 'new-instance v0, Ljava/util/HashMap;', 'invoke-direct {v0}, Ljava/util/HashMap;-><init>()V', 'const-string v1, "com.baidu.input_mi/.ImeService"', 'invoke-static {p0, v1}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z', 'const-string v2, "input_method"'],
        'type': 'method_replace',
        'search': """.method public static rdInputmethodEvent(Ljava/lang/String;)V
    .registers 4

    sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z

    if-nez v0, :cond_0

    return-void

    :cond_0
    new-instance v0, Ljava/util/HashMap;

    invoke-direct {v0}, Ljava/util/HashMap;-><init>()V

    const-string v1, "com.baidu.input_mi/.ImeService"

    invoke-static {p0, v1}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v1

    const-string v2, "input_method"

    if-eqz v1, :cond_1

    const-string p0, "baidu"

    invoke-interface {v0, v2, p0}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_0

    :cond_1
    const-string v1, "com.sohu.inputmethod.sogou.xiaomi/.SogouIME"

    invoke-static {p0, v1}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p0

    if-eqz p0, :cond_2

    const-string p0, "sougou"

    invoke-interface {v0, v2, p0}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    :cond_2
    :goto_0
    const-string p0, "choose_input_method"

    invoke-static {p0, v0}, Lcom/android/provision/utils/OTHelper;->tkEvent(Ljava/lang/String;Ljava/util/Map;)V

    return-void
.end method""",
        'replacement': """.method public static rdInputmethodEvent(Ljava/lang/String;)V
    .registers 1

    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_utils_OTHelper__rdPageStayTimeEvent',
        'method': '.method public static rdPageStayTimeEvent(Ljava/lang/String;J)V',
        'method_name': 'rdPageStayTimeEvent',
        'method_anchors': ['sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z', 'if-eqz v0, :cond_1', 'invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z', 'if-eqz v0, :cond_0', 'new-instance v0, Ljava/util/HashMap;', 'invoke-direct {v0}, Ljava/util/HashMap;-><init>()V', 'new-instance v1, Ljava/lang/StringBuilder;', 'invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V'],
        'type': 'method_replace',
        'search': """.method public static rdPageStayTimeEvent(Ljava/lang/String;J)V
    .registers 5

    sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z

    if-eqz v0, :cond_1

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    new-instance v0, Ljava/util/HashMap;

    invoke-direct {v0}, Ljava/util/HashMap;-><init>()V

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string p0, "_"

    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {p1, p2}, Ljava/lang/String;->valueOf(J)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const-string p1, "stay_time"

    invoke-interface {v0, p1, p0}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string p0, "page_stay_time"

    invoke-static {p0, v0}, Lcom/android/provision/utils/OTHelper;->tkEvent(Ljava/lang/String;Ljava/util/Map;)V

    :cond_1
    :goto_0
    return-void
.end method""",
        'replacement': """.method public static rdPageStayTimeEvent(Ljava/lang/String;J)V
    .registers 3

    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_utils_OTHelper__rdProvisionNetType',
        'method': '.method public static rdProvisionNetType()V',
        'method_name': 'rdProvisionNetType',
        'method_anchors': ['sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z', 'if-nez v0, :cond_0', 'invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;', 'if-nez v0, :cond_1', 'return-void', 'invoke-static {v0}, Lmiuix/net/ConnectivityHelper;->getInstance(Landroid/content/Context;)Lmiuix/net/ConnectivityHelper;', 'invoke-virtual {v1}, Lmiuix/net/ConnectivityHelper;->isNetworkConnected()Z', 'if-eqz v1, :cond_3'],
        'type': 'method_replace',
        'search': """.method public static rdProvisionNetType()V
    .registers 3

    sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    if-nez v0, :cond_1

    :goto_0
    return-void

    :cond_1
    invoke-static {v0}, Lmiuix/net/ConnectivityHelper;->getInstance(Landroid/content/Context;)Lmiuix/net/ConnectivityHelper;

    move-result-object v1

    invoke-virtual {v1}, Lmiuix/net/ConnectivityHelper;->isNetworkConnected()Z

    move-result v1

    if-eqz v1, :cond_3

    invoke-static {v0}, Lmiuix/net/ConnectivityHelper;->getInstance(Landroid/content/Context;)Lmiuix/net/ConnectivityHelper;

    move-result-object v0

    invoke-virtual {v0}, Lmiuix/net/ConnectivityHelper;->isUnmeteredNetworkConnected()Z

    move-result v0

    if-eqz v0, :cond_2

    const-string v0, "network_wifi"

    goto :goto_1

    :cond_2
    const-string v0, "network_data"

    goto :goto_1

    :cond_3
    const-string v0, "network_none"

    :goto_1
    new-instance v1, Ljava/util/HashMap;

    invoke-direct {v1}, Ljava/util/HashMap;-><init>()V

    const-string v2, "network_stat"

    invoke-interface {v1, v2, v0}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v0, "key_click_complete_done"

    invoke-static {v0, v1}, Lcom/android/provision/utils/OTHelper;->tkEvent(Ljava/lang/String;Ljava/util/Map;)V

    return-void
.end method""",
        'replacement': """.method public static rdProvisionNetType()V
    .registers 0

    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_utils_OTHelper__setNetworkAccessEnabled',
        'method': '.method public static setNetworkAccessEnabled(Landroid/content/Context;)V',
        'method_name': 'setNetworkAccessEnabled',
        'method_anchors': ['sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z', 'if-nez v0, :cond_0', 'return-void', 'invoke-static {p0, v0}, Lcom/xiaomi/onetrack/OneTrack;->setAccessNetworkEnable(Landroid/content/Context;Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method public static setNetworkAccessEnabled(Landroid/content/Context;)V
    .registers 2

    sget-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z

    if-nez v0, :cond_0

    return-void

    :cond_0
    const/4 v0, 0x1

    invoke-static {p0, v0}, Lcom/xiaomi/onetrack/OneTrack;->setAccessNetworkEnable(Landroid/content/Context;Z)V

    return-void
.end method""",
        'replacement': """.method public static setNetworkAccessEnabled(Landroid/content/Context;)V
    .registers 1

    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_utils_OTHelper__clinit',
        'method': '.method static constructor <clinit>()V',
        'method_name': '<clinit>',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'sput-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z', 'new-instance v0, Ljava/util/concurrent/atomic/AtomicBoolean;', 'invoke-direct {v0, v2}, Ljava/util/concurrent/atomic/AtomicBoolean;-><init>(Z)V', 'sput-object v0, Lcom/android/provision/utils/OTHelper;->sInited:Ljava/util/concurrent/atomic/AtomicBoolean;', 'new-instance v0, Lcom/xiaomi/onetrack/Configuration$Builder;', 'invoke-direct {v0}, Lcom/xiaomi/onetrack/Configuration$Builder;-><init>()V', 'const-string v2, "31000000387"'],
        'type': 'method_delete',
        'search': """.method static constructor <clinit>()V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x1

    xor-int/2addr v0, v1

    sput-boolean v0, Lcom/android/provision/utils/OTHelper;->IS_ENABLE:Z

    new-instance v0, Ljava/util/concurrent/atomic/AtomicBoolean;

    const/4 v2, 0x0

    invoke-direct {v0, v2}, Ljava/util/concurrent/atomic/AtomicBoolean;-><init>(Z)V

    sput-object v0, Lcom/android/provision/utils/OTHelper;->sInited:Ljava/util/concurrent/atomic/AtomicBoolean;

    new-instance v0, Lcom/xiaomi/onetrack/Configuration$Builder;

    invoke-direct {v0}, Lcom/xiaomi/onetrack/Configuration$Builder;-><init>()V

    const-string v2, "31000000387"

    invoke-virtual {v0, v2}, Lcom/xiaomi/onetrack/Configuration$Builder;->setAppId(Ljava/lang/String;)Lcom/xiaomi/onetrack/Configuration$Builder;

    move-result-object v0

    const-string v2, "xiaomi"

    invoke-virtual {v0, v2}, Lcom/xiaomi/onetrack/Configuration$Builder;->setChannel(Ljava/lang/String;)Lcom/xiaomi/onetrack/Configuration$Builder;

    move-result-object v0

    invoke-virtual {v0, v1}, Lcom/xiaomi/onetrack/Configuration$Builder;->setExceptionCatcherEnable(Z)Lcom/xiaomi/onetrack/Configuration$Builder;

    move-result-object v0

    sget-object v1, Lcom/xiaomi/onetrack/OneTrack$Mode;->APP:Lcom/xiaomi/onetrack/OneTrack$Mode;

    invoke-virtual {v0, v1}, Lcom/xiaomi/onetrack/Configuration$Builder;->setMode(Lcom/xiaomi/onetrack/OneTrack$Mode;)Lcom/xiaomi/onetrack/Configuration$Builder;

    move-result-object v0

    invoke-virtual {v0}, Lcom/xiaomi/onetrack/Configuration$Builder;->build()Lcom/xiaomi/onetrack/Configuration;

    move-result-object v0

    sput-object v0, Lcom/android/provision/utils/OTHelper;->mConfig:Lcom/xiaomi/onetrack/Configuration;

    return-void
.end method""",
        'replacement': """""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
