TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/pinyin/utilities/HindiPinyinConverter$1.smali'
CLASS_FALLBACK_NAMES = ['HindiPinyinConverter$1.smali']
CLASS_ANCHORS = ['.super Lmiuix/core/util/SoftReferenceSingleton;']

PATCHES = [
    {
        'id': 'miuix_pinyin_utilities_HindiPinyinConverter__1__createInstance',
        'method': '.method protected bridge synthetic createInstance()Ljava/lang/Object;',
        'method_name': 'createInstance',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/pinyin/utilities/HindiPinyinConverter$1;->createInstance()Lmiuix/pinyin/utilities/HindiPinyinConverter;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic createInstance()Ljava/lang/Object;
    .registers 1

    invoke-virtual {p0}, Lmiuix/pinyin/utilities/HindiPinyinConverter$1;->createInstance()Lmiuix/pinyin/utilities/HindiPinyinConverter;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic createInstance()Ljava/lang/Object;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-virtual {p0}, Lmiuix/pinyin/utilities/HindiPinyinConverter$1;->createInstance()Lmiuix/pinyin/utilities/HindiPinyinConverter;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pinyin_utilities_HindiPinyinConverter__1__createInstance',
        'method': '.method protected createInstance()Lmiuix/pinyin/utilities/HindiPinyinConverter;',
        'method_name': 'createInstance',
        'method_anchors': ['new-instance p0, Lmiuix/pinyin/utilities/HindiPinyinConverter;', 'invoke-direct {p0, v0}, Lmiuix/pinyin/utilities/HindiPinyinConverter;-><init>(Lmiuix/pinyin/utilities/HindiPinyinConverter$1;)V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected createInstance()Lmiuix/pinyin/utilities/HindiPinyinConverter;
    .registers 2

    new-instance p0, Lmiuix/pinyin/utilities/HindiPinyinConverter;

    const/4 v0, 0x0

    invoke-direct {p0, v0}, Lmiuix/pinyin/utilities/HindiPinyinConverter;-><init>(Lmiuix/pinyin/utilities/HindiPinyinConverter$1;)V

    return-object p0
.end method""",
        'replacement': """.method protected createInstance()Lmiuix/pinyin/utilities/HindiPinyinConverter;
    .registers 2

    goto :goto_2

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-direct {p0, v0}, Lmiuix/pinyin/utilities/HindiPinyinConverter;-><init>(Lmiuix/pinyin/utilities/HindiPinyinConverter$1;)V

    goto :goto_0

    nop

    :goto_2
    new-instance p0, Lmiuix/pinyin/utilities/HindiPinyinConverter;

    goto :goto_3

    nop

    :goto_3
    const/4 v0, 0x0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
