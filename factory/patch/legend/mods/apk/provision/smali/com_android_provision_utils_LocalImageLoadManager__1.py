TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/utils/LocalImageLoadManager$1.smali'
CLASS_FALLBACK_NAMES = ['LocalImageLoadManager$1.smali']
CLASS_ANCHORS = ['.super Landroid/util/LruCache;']

PATCHES = [
    {
        'id': 'com_android_provision_utils_LocalImageLoadManager__1__sizeOf',
        'method': '.method protected bridge synthetic sizeOf(Ljava/lang/Object;Ljava/lang/Object;)I',
        'method_name': 'sizeOf',
        'method_anchors': ['check-cast p1, Ljava/lang/Integer;', 'check-cast p2, Landroid/graphics/drawable/Drawable;', 'invoke-virtual {p0, p1, p2}, Lcom/android/provision/utils/LocalImageLoadManager$1;->sizeOf(Ljava/lang/Integer;Landroid/graphics/drawable/Drawable;)I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic sizeOf(Ljava/lang/Object;Ljava/lang/Object;)I
    .registers 3

    check-cast p1, Ljava/lang/Integer;

    check-cast p2, Landroid/graphics/drawable/Drawable;

    invoke-virtual {p0, p1, p2}, Lcom/android/provision/utils/LocalImageLoadManager$1;->sizeOf(Ljava/lang/Integer;Landroid/graphics/drawable/Drawable;)I

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected bridge synthetic sizeOf(Ljava/lang/Object;Ljava/lang/Object;)I
    .registers 3

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0, p1, p2}, Lcom/android/provision/utils/LocalImageLoadManager$1;->sizeOf(Ljava/lang/Integer;Landroid/graphics/drawable/Drawable;)I

    move-result p0

    goto :goto_2

    nop

    :goto_1
    check-cast p1, Ljava/lang/Integer;

    goto :goto_3

    nop

    :goto_2
    return p0

    :goto_3
    check-cast p2, Landroid/graphics/drawable/Drawable;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_utils_LocalImageLoadManager__1__sizeOf',
        'method': '.method protected sizeOf(Ljava/lang/Integer;Landroid/graphics/drawable/Drawable;)I',
        'method_name': 'sizeOf',
        'method_anchors': ['invoke-static {p2}, Lcom/android/provision/utils/LocalImageLoadManager;->getDrawableByteSize(Landroid/graphics/drawable/Drawable;)I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected sizeOf(Ljava/lang/Integer;Landroid/graphics/drawable/Drawable;)I
    .registers 3

    invoke-static {p2}, Lcom/android/provision/utils/LocalImageLoadManager;->getDrawableByteSize(Landroid/graphics/drawable/Drawable;)I

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected sizeOf(Ljava/lang/Integer;Landroid/graphics/drawable/Drawable;)I
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    invoke-static {p2}, Lcom/android/provision/utils/LocalImageLoadManager;->getDrawableByteSize(Landroid/graphics/drawable/Drawable;)I

    move-result p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
