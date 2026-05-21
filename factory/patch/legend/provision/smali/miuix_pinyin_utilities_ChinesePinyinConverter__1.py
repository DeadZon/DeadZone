TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/pinyin/utilities/ChinesePinyinConverter$1.smali'
CLASS_FALLBACK_NAMES = ['ChinesePinyinConverter$1.smali']
CLASS_ANCHORS = ['.super Lmiuix/core/util/SoftReferenceSingleton;']

PATCHES = [
    {
        'id': 'miuix_pinyin_utilities_ChinesePinyinConverter__1__createInstance',
        'method': '.method protected bridge synthetic createInstance(Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'createInstance',
        'method_anchors': ['invoke-virtual {p0, p1}, Lmiuix/pinyin/utilities/ChinesePinyinConverter$1;->createInstance(Ljava/lang/Object;)Lmiuix/pinyin/utilities/ChinesePinyinConverter;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic createInstance(Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    invoke-virtual {p0, p1}, Lmiuix/pinyin/utilities/ChinesePinyinConverter$1;->createInstance(Ljava/lang/Object;)Lmiuix/pinyin/utilities/ChinesePinyinConverter;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic createInstance(Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0, p1}, Lmiuix/pinyin/utilities/ChinesePinyinConverter$1;->createInstance(Ljava/lang/Object;)Lmiuix/pinyin/utilities/ChinesePinyinConverter;

    move-result-object p0

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pinyin_utilities_ChinesePinyinConverter__1__createInstance',
        'method': '.method protected createInstance(Ljava/lang/Object;)Lmiuix/pinyin/utilities/ChinesePinyinConverter;',
        'method_name': 'createInstance',
        'method_anchors': ['new-instance p0, Lmiuix/pinyin/utilities/ChinesePinyinConverter;', 'check-cast p1, Landroid/content/Context;', 'invoke-direct {p0, p1, v0}, Lmiuix/pinyin/utilities/ChinesePinyinConverter;-><init>(Landroid/content/Context;Lmiuix/pinyin/utilities/ChinesePinyinConverter$1;)V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected createInstance(Ljava/lang/Object;)Lmiuix/pinyin/utilities/ChinesePinyinConverter;
    .registers 3

    new-instance p0, Lmiuix/pinyin/utilities/ChinesePinyinConverter;

    check-cast p1, Landroid/content/Context;

    const/4 v0, 0x0

    invoke-direct {p0, p1, v0}, Lmiuix/pinyin/utilities/ChinesePinyinConverter;-><init>(Landroid/content/Context;Lmiuix/pinyin/utilities/ChinesePinyinConverter$1;)V

    return-object p0
.end method""",
        'replacement': """.method protected createInstance(Ljava/lang/Object;)Lmiuix/pinyin/utilities/ChinesePinyinConverter;
    .registers 3

    goto :goto_3

    nop

    :goto_0
    invoke-direct {p0, p1, v0}, Lmiuix/pinyin/utilities/ChinesePinyinConverter;-><init>(Landroid/content/Context;Lmiuix/pinyin/utilities/ChinesePinyinConverter$1;)V

    goto :goto_1

    nop

    :goto_1
    return-object p0

    :goto_2
    const/4 v0, 0x0

    goto :goto_0

    nop

    :goto_3
    new-instance p0, Lmiuix/pinyin/utilities/ChinesePinyinConverter;

    goto :goto_4

    nop

    :goto_4
    check-cast p1, Landroid/content/Context;

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
