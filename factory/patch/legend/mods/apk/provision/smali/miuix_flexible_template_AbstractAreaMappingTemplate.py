TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/flexible/template/AbstractAreaMappingTemplate.smali'
CLASS_FALLBACK_NAMES = ['AbstractAreaMappingTemplate.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lmiuix/flexible/template/IHyperCellTemplate;']

PATCHES = [
    {
        'id': 'miuix_flexible_template_AbstractAreaMappingTemplate__findViewByAreaId',
        'method': '.method protected findViewByAreaId(Landroid/view/ViewGroup;I)Landroid/view/View;',
        'method_name': 'findViewByAreaId',
        'method_anchors': ['if-eqz p0, :cond_0', 'check-cast p1, Lmiuix/flexible/view/HyperCellLayout;', 'invoke-virtual {p1, p2}, Lmiuix/flexible/view/HyperCellLayout;->findViewByAreaId(I)Landroid/view/View;', 'return-object p0', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected findViewByAreaId(Landroid/view/ViewGroup;I)Landroid/view/View;
    .registers 3

    instance-of p0, p1, Lmiuix/flexible/view/HyperCellLayout;

    if-eqz p0, :cond_0

    check-cast p1, Lmiuix/flexible/view/HyperCellLayout;

    invoke-virtual {p1, p2}, Lmiuix/flexible/view/HyperCellLayout;->findViewByAreaId(I)Landroid/view/View;

    move-result-object p0

    return-object p0

    :cond_0
    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method protected findViewByAreaId(Landroid/view/ViewGroup;I)Landroid/view/View;
    .registers 3

    goto :goto_6

    nop

    :goto_0
    return-object p0

    :goto_1
    goto :goto_5

    nop

    :goto_2
    if-nez p0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_3

    nop

    :goto_3
    check-cast p1, Lmiuix/flexible/view/HyperCellLayout;

    goto :goto_4

    nop

    :goto_4
    invoke-virtual {p1, p2}, Lmiuix/flexible/view/HyperCellLayout;->findViewByAreaId(I)Landroid/view/View;

    move-result-object p0

    goto :goto_0

    nop

    :goto_5
    const/4 p0, 0x0

    goto :goto_7

    nop

    :goto_6
    instance-of p0, p1, Lmiuix/flexible/view/HyperCellLayout;

    goto :goto_2

    nop

    :goto_7
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
