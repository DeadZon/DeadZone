TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/pinyin/utilities/ChinesePinyinConverter$ChinesePinyinDictionary.smali'
CLASS_FALLBACK_NAMES = ['ChinesePinyinConverter$ChinesePinyinDictionary.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_pinyin_utilities_ChinesePinyinConverter__ChinesePinyinDictionary__finalize',
        'method': '.method protected finalize()V',
        'method_name': 'finalize',
        'method_anchors': ['iget-object v0, p0, Lmiuix/pinyin/utilities/ChinesePinyinConverter$ChinesePinyinDictionary;->mReader:Lmiuix/core/util/DirectIndexedFile$Reader;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Lmiuix/core/util/DirectIndexedFile$Reader;->close()V', 'invoke-super {p0}, Ljava/lang/Object;->finalize()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected finalize()V
    .registers 2

    iget-object v0, p0, Lmiuix/pinyin/utilities/ChinesePinyinConverter$ChinesePinyinDictionary;->mReader:Lmiuix/core/util/DirectIndexedFile$Reader;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Lmiuix/core/util/DirectIndexedFile$Reader;->close()V

    :cond_0
    invoke-super {p0}, Ljava/lang/Object;->finalize()V

    return-void
.end method""",
        'replacement': """.method protected finalize()V
    .registers 2

    goto :goto_4

    nop

    :goto_0
    invoke-super {p0}, Ljava/lang/Object;->finalize()V

    goto :goto_5

    nop

    :goto_1
    invoke-virtual {v0}, Lmiuix/core/util/DirectIndexedFile$Reader;->close()V

    :goto_2
    goto :goto_0

    nop

    :goto_3
    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/pinyin/utilities/ChinesePinyinConverter$ChinesePinyinDictionary;->mReader:Lmiuix/core/util/DirectIndexedFile$Reader;

    goto :goto_3

    nop

    :goto_5
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
