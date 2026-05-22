TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/utils/CarouselUtils$4.smali'
CLASS_FALLBACK_NAMES = ['CarouselUtils$4.smali']
CLASS_ANCHORS = ['.super Landroid/os/AsyncTask;']

PATCHES = [
    {
        'id': 'com_android_provision_utils_CarouselUtils__4__doInBackground',
        'method': '.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'doInBackground',
        'method_anchors': ['check-cast p1, [Ljava/lang/Void;', 'invoke-virtual {p0, p1}, Lcom/android/provision/utils/CarouselUtils$4;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    check-cast p1, [Ljava/lang/Void;

    invoke-virtual {p0, p1}, Lcom/android/provision/utils/CarouselUtils$4;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    goto :goto_0

    nop

    :goto_0
    check-cast p1, [Ljava/lang/Void;

    goto :goto_2

    nop

    :goto_1
    return-object p0

    :goto_2
    invoke-virtual {p0, p1}, Lcom/android/provision/utils/CarouselUtils$4;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;

    move-result-object p0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_utils_CarouselUtils__4__doInBackground',
        'method': '.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;',
        'method_name': 'doInBackground',
        'method_anchors': ['iget-object p1, p0, Lcom/android/provision/utils/CarouselUtils$4;->val$context:Landroid/content/Context;', 'iget-object p0, p0, Lcom/android/provision/utils/CarouselUtils$4;->val$message:Lcom/android/provision/beans/CarouselProvisionMessageBean;', 'invoke-static {p1, p0}, Lcom/android/provision/utils/CarouselUtils;->-$$Nest$smsetCarouselInfo(Landroid/content/Context;Lcom/android/provision/beans/CarouselProvisionMessageBean;)V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;
    .registers 2

    iget-object p1, p0, Lcom/android/provision/utils/CarouselUtils$4;->val$context:Landroid/content/Context;

    iget-object p0, p0, Lcom/android/provision/utils/CarouselUtils$4;->val$message:Lcom/android/provision/beans/CarouselProvisionMessageBean;

    invoke-static {p1, p0}, Lcom/android/provision/utils/CarouselUtils;->-$$Nest$smsetCarouselInfo(Landroid/content/Context;Lcom/android/provision/beans/CarouselProvisionMessageBean;)V

    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;
    .registers 2

    goto :goto_1

    nop

    :goto_0
    invoke-static {p1, p0}, Lcom/android/provision/utils/CarouselUtils;->-$$Nest$smsetCarouselInfo(Landroid/content/Context;Lcom/android/provision/beans/CarouselProvisionMessageBean;)V

    goto :goto_2

    nop

    :goto_1
    iget-object p1, p0, Lcom/android/provision/utils/CarouselUtils$4;->val$context:Landroid/content/Context;

    goto :goto_4

    nop

    :goto_2
    const/4 p0, 0x0

    goto :goto_3

    nop

    :goto_3
    return-object p0

    :goto_4
    iget-object p0, p0, Lcom/android/provision/utils/CarouselUtils$4;->val$message:Lcom/android/provision/beans/CarouselProvisionMessageBean;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
