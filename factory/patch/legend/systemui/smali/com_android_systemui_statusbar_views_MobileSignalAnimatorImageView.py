"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/views/MobileSignalAnimatorImageView.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/views/MobileSignalAnimatorImageView.smali'
CLASS_FALLBACK_NAMES = ['MobileSignalAnimatorImageView.smali']
CLASS_ANCHORS        = ['invoke-direct/range {v0 .. v6}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;IIILkotlin/jvm/internal/DefaultConstructorMarker;)V', 'invoke-direct/range {v0 .. v6}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;IIILkotlin/jvm/internal/DefaultConstructorMarker;)V', 'invoke-direct/range {v0 .. v6}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;IIILkotlin/jvm/internal/DefaultConstructorMarker;)V', 'invoke-direct {p0, p1, p2, p3, p4}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V', 'iput p1, p0, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorImageView;->islandState:I']

PATCHES = [
    {
        'id':             'p0000_copyView',
        'type':           'method_add',
        'method':         '.method public copyView()Landroid/view/View;',
        'method_name':    'copyView',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/ImageView;->getContext()Landroid/content/Context;', 'invoke-direct/range {v0 .. v6}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;IIILkotlin/jvm/internal/DefaultConstructorMarker;)V', 'invoke-virtual {p0}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;'],
        'search':         None,
        'replacement':    '.method public copyView()Landroid/view/View;\n    .registers 8\n\n    new-instance v0, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorImageView;\n\n    invoke-virtual {p0}, Landroid/widget/ImageView;->getContext()Landroid/content/Context;\n\n    move-result-object v1\n\n    const/16 v5, 0xe\n\n    const/4 v6, 0x0\n\n    const/4 v2, 0x0\n\n    const/4 v3, 0x0\n\n    const/4 v4, 0x0\n\n    invoke-direct/range {v0 .. v6}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;IIILkotlin/jvm/internal/DefaultConstructorMarker;)V\n\n    invoke-virtual {p0}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;\n\n    move-result-object v1\n\n    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V\n\n    invoke-virtual {p0}, Landroid/widget/ImageView;->getAdjustViewBounds()Z\n\n    move-result p0\n\n    invoke-virtual {v0, p0}, Landroid/widget/ImageView;->setAdjustViewBounds(Z)V\n\n    return-object v0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
]
