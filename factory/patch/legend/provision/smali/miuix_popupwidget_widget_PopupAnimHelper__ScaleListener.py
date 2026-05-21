TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/popupwidget/widget/PopupAnimHelper$ScaleListener.smali'
CLASS_FALLBACK_NAMES = ['PopupAnimHelper$ScaleListener.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/listener/TransitionListener;']

PATCHES = [
    {
        'id': 'miuix_popupwidget_widget_PopupAnimHelper__ScaleListener__setDimValue',
        'method': '.method setDimValue(F)V',
        'method_name': 'setDimValue',
        'method_anchors': ['iput p1, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mTargetDim:F', 'return-void'],
        'type': 'method_replace',
        'search': """.method setDimValue(F)V
    .registers 2

    iput p1, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mTargetDim:F

    return-void
.end method""",
        'replacement': """.method setDimValue(F)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput p1, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mTargetDim:F

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupAnimHelper__ScaleListener__updateScaleBounds',
        'method': '.method updateScaleBounds(Landroid/graphics/Rect;II)V',
        'method_name': 'updateScaleBounds',
        'method_anchors': ['invoke-direct {p0, p1, p2, p3}, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->getStartBounds(Landroid/graphics/Rect;II)Landroid/graphics/Rect;', 'iget p3, p1, Landroid/graphics/Rect;->left:I', 'iput p3, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mEndLeft:I', 'iget p3, p1, Landroid/graphics/Rect;->top:I', 'iput p3, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mEndTop:I', 'iget p3, p1, Landroid/graphics/Rect;->right:I', 'iput p3, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mEndRight:I', 'iget p1, p1, Landroid/graphics/Rect;->bottom:I'],
        'type': 'method_replace',
        'search': """.method updateScaleBounds(Landroid/graphics/Rect;II)V
    .registers 4

    invoke-direct {p0, p1, p2, p3}, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->getStartBounds(Landroid/graphics/Rect;II)Landroid/graphics/Rect;

    move-result-object p2

    iget p3, p1, Landroid/graphics/Rect;->left:I

    iput p3, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mEndLeft:I

    iget p3, p1, Landroid/graphics/Rect;->top:I

    iput p3, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mEndTop:I

    iget p3, p1, Landroid/graphics/Rect;->right:I

    iput p3, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mEndRight:I

    iget p1, p1, Landroid/graphics/Rect;->bottom:I

    iput p1, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mEndBottom:I

    iget p1, p2, Landroid/graphics/Rect;->left:I

    iput p1, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mStartLeft:I

    iget p1, p2, Landroid/graphics/Rect;->top:I

    iput p1, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mStartTop:I

    iget p1, p2, Landroid/graphics/Rect;->right:I

    iput p1, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mStartRight:I

    iget p1, p2, Landroid/graphics/Rect;->bottom:I

    iput p1, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mStartBottom:I

    return-void
.end method""",
        'replacement': """.method updateScaleBounds(Landroid/graphics/Rect;II)V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    iget p1, p2, Landroid/graphics/Rect;->left:I

    goto :goto_5

    nop

    :goto_1
    iput p3, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mEndLeft:I

    goto :goto_10

    nop

    :goto_2
    invoke-direct {p0, p1, p2, p3}, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->getStartBounds(Landroid/graphics/Rect;II)Landroid/graphics/Rect;

    move-result-object p2

    goto :goto_6

    nop

    :goto_3
    iput p3, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mEndTop:I

    goto :goto_7

    nop

    :goto_4
    iput p1, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mStartBottom:I

    goto :goto_b

    nop

    :goto_5
    iput p1, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mStartLeft:I

    goto :goto_d

    nop

    :goto_6
    iget p3, p1, Landroid/graphics/Rect;->left:I

    goto :goto_1

    nop

    :goto_7
    iget p3, p1, Landroid/graphics/Rect;->right:I

    goto :goto_9

    nop

    :goto_8
    iget p1, p1, Landroid/graphics/Rect;->bottom:I

    goto :goto_c

    nop

    :goto_9
    iput p3, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mEndRight:I

    goto :goto_8

    nop

    :goto_a
    iget p1, p2, Landroid/graphics/Rect;->right:I

    goto :goto_11

    nop

    :goto_b
    return-void

    :goto_c
    iput p1, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mEndBottom:I

    goto :goto_0

    nop

    :goto_d
    iget p1, p2, Landroid/graphics/Rect;->top:I

    goto :goto_e

    nop

    :goto_e
    iput p1, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mStartTop:I

    goto :goto_a

    nop

    :goto_f
    iget p1, p2, Landroid/graphics/Rect;->bottom:I

    goto :goto_4

    nop

    :goto_10
    iget p3, p1, Landroid/graphics/Rect;->top:I

    goto :goto_3

    nop

    :goto_11
    iput p1, p0, Lmiuix/popupwidget/widget/PopupAnimHelper$ScaleListener;->mStartRight:I

    goto :goto_f

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
