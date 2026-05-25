TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/spring/view/SpringHelper$2.smali'
CLASS_FALLBACK_NAMES = ['SpringHelper$2.smali']
CLASS_ANCHORS = ['.super Lmiuix/spring/view/SpringHelper$AxisHandler;']

PATCHES = [
    {
        'id': 'miuix_spring_view_SpringHelper__2__onFlingReachEdge',
        'method': '.method onFlingReachEdge()V',
        'method_name': 'onFlingReachEdge',
        'method_anchors': ['iget-object p0, p0, Lmiuix/spring/view/SpringHelper$2;->this$0:Lmiuix/spring/view/SpringHelper;', 'invoke-virtual {p0}, Lmiuix/spring/view/SpringHelper;->vibrate()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method onFlingReachEdge()V
    .registers 1

    iget-object p0, p0, Lmiuix/spring/view/SpringHelper$2;->this$0:Lmiuix/spring/view/SpringHelper;

    invoke-virtual {p0}, Lmiuix/spring/view/SpringHelper;->vibrate()V

    return-void
.end method""",
        'replacement': """.method onFlingReachEdge()V
    .registers 1

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/spring/view/SpringHelper;->vibrate()V

    goto :goto_1

    nop

    :goto_1
    return-void

    :goto_2
    iget-object p0, p0, Lmiuix/spring/view/SpringHelper$2;->this$0:Lmiuix/spring/view/SpringHelper;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_spring_view_SpringHelper__2__canScroll',
        'method': '.method protected canScroll()Z',
        'method_name': 'canScroll',
        'method_anchors': ['iget-object p0, p0, Lmiuix/spring/view/SpringHelper$2;->this$0:Lmiuix/spring/view/SpringHelper;', 'invoke-virtual {p0}, Lmiuix/spring/view/SpringHelper;->canScrollVertically()Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected canScroll()Z
    .registers 1

    iget-object p0, p0, Lmiuix/spring/view/SpringHelper$2;->this$0:Lmiuix/spring/view/SpringHelper;

    invoke-virtual {p0}, Lmiuix/spring/view/SpringHelper;->canScrollVertically()Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected canScroll()Z
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/spring/view/SpringHelper$2;->this$0:Lmiuix/spring/view/SpringHelper;

    goto :goto_2

    nop

    :goto_1
    return p0

    :goto_2
    invoke-virtual {p0}, Lmiuix/spring/view/SpringHelper;->canScrollVertically()Z

    move-result p0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_spring_view_SpringHelper__2__getSize',
        'method': '.method protected getSize()I',
        'method_name': 'getSize',
        'method_anchors': ['iget-object p0, p0, Lmiuix/spring/view/SpringHelper$2;->this$0:Lmiuix/spring/view/SpringHelper;', 'invoke-virtual {p0}, Lmiuix/spring/view/SpringHelper;->getHeight()I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getSize()I
    .registers 1

    iget-object p0, p0, Lmiuix/spring/view/SpringHelper$2;->this$0:Lmiuix/spring/view/SpringHelper;

    invoke-virtual {p0}, Lmiuix/spring/view/SpringHelper;->getHeight()I

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected getSize()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/spring/view/SpringHelper$2;->this$0:Lmiuix/spring/view/SpringHelper;

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0}, Lmiuix/spring/view/SpringHelper;->getHeight()I

    move-result p0

    goto :goto_2

    nop

    :goto_2
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
