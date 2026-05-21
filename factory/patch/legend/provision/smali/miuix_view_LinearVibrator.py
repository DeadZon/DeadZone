TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/view/LinearVibrator.smali'
CLASS_FALLBACK_NAMES = ['LinearVibrator.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lmiuix/view/HapticFeedbackProvider;', '.field private static final TAG:Ljava/lang/String; = "LinearVibrator"']

PATCHES = [
    {
        'id': 'miuix_view_LinearVibrator__obtainFeedBack',
        'method': '.method obtainFeedBack(I)I',
        'method_name': 'obtainFeedBack',
        'method_anchors': ['iget-object v0, p0, Lmiuix/view/LinearVibrator;->mIds:Landroidx/collection/SparseArrayCompat;', 'invoke-virtual {v0, p1}, Landroidx/collection/SparseArrayCompat;->indexOfKey(I)I', 'if-ltz p1, :cond_0', 'iget-object p0, p0, Lmiuix/view/LinearVibrator;->mIds:Landroidx/collection/SparseArrayCompat;', 'invoke-virtual {p0, p1}, Landroidx/collection/SparseArrayCompat;->valueAt(I)Ljava/lang/Object;', 'check-cast p0, Ljava/lang/Integer;', 'invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I', 'return p0'],
        'type': 'method_replace',
        'search': """.method obtainFeedBack(I)I
    .registers 3

    iget-object v0, p0, Lmiuix/view/LinearVibrator;->mIds:Landroidx/collection/SparseArrayCompat;

    invoke-virtual {v0, p1}, Landroidx/collection/SparseArrayCompat;->indexOfKey(I)I

    move-result p1

    if-ltz p1, :cond_0

    iget-object p0, p0, Lmiuix/view/LinearVibrator;->mIds:Landroidx/collection/SparseArrayCompat;

    invoke-virtual {p0, p1}, Landroidx/collection/SparseArrayCompat;->valueAt(I)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Ljava/lang/Integer;

    invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    return p0

    :cond_0
    const/4 p0, -0x1

    return p0
.end method""",
        'replacement': """.method obtainFeedBack(I)I
    .registers 3

    goto :goto_1

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/view/LinearVibrator;->mIds:Landroidx/collection/SparseArrayCompat;

    goto :goto_9

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/view/LinearVibrator;->mIds:Landroidx/collection/SparseArrayCompat;

    goto :goto_5

    nop

    :goto_2
    return p0

    :goto_3
    goto :goto_7

    nop

    :goto_4
    check-cast p0, Ljava/lang/Integer;

    goto :goto_a

    nop

    :goto_5
    invoke-virtual {v0, p1}, Landroidx/collection/SparseArrayCompat;->indexOfKey(I)I

    move-result p1

    goto :goto_8

    nop

    :goto_6
    return p0

    :goto_7
    const/4 p0, -0x1

    goto :goto_6

    nop

    :goto_8
    if-gez p1, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_0

    nop

    :goto_9
    invoke-virtual {p0, p1}, Landroidx/collection/SparseArrayCompat;->valueAt(I)Ljava/lang/Object;

    move-result-object p0

    goto :goto_4

    nop

    :goto_a
    invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
